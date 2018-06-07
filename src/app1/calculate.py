from django.shortcuts import render
from .models import *
from django.db.models import Count, F, Sum
from abc import ABC, abstractmethod
import re
from datetime import datetime,timedelta

class Trait(ABC):
    '''
        Objective: An abstract class which calculates the value of the trait and stores it in the database.
    '''

    def __init__(self, trait_cmp):
        '''
        Objective: A constructor which initializes the trait component variable.
        Input Parameter: trait_cmp - Trait Component
        Return Value: Returns an object of the called class
        '''
        self.trait_component = trait_cmp

    def template_method(self, trait_name, trait_value, traitWeightageList,recommendation_list,request):
        '''
        Objective: Template method defines an algorithm's skeleton in the Trait base class
                    and let subclasses redefine certain steps of the algorithm.
        Input Parameter: trait_list - A list of Traits
                         value_list - A list of Values of the corresponding traits defined in the trait_list
        '''
        table_name = self.find_table()
        self.store_sid(table_name,request)
        value = self.calc_value(request)
        traitWeightage = self.returnTraitWeightage()
        traitWeightageList.append(traitWeightage)
        self.saveRecommendation(value, recommendation_list,request)
        self.store_value(value, table_name, trait_name, trait_value,request)
        self.calc_overall_health(trait_value,traitWeightageList,request)
        #self.store_overall_value(TraitValueDetails,overall_value_health,request)

    def find_table(self):
        '''
        Objective: To find the database table which contains the trait_component field .
        Return Value: Returns the database table name
        '''
        for cls in BaseTraitDetails.__subclasses__():
            field=cls._meta.get_field(self.trait_component)
            if field:
                return cls

    def store_sid(self,table_name,request):
        '''
        Objective: To check and then store the sid of seller in the table_name which contains trait_component.
        Input Parameter: table_name - Table which contains trait_component
        '''
        check=table_name.objects.filter(sid=request.user).exists()
        if check==False:
            #s=SellerDetails.objects.get(sid=request.user)
            save_sid=table_name(sid=request.user)
            save_sid.save()

    @abstractmethod
    def calc_value(self):
        '''
        Objective: An abstract method which calculates the value of trait_component.
        Return Value: Calculated Value of the trait.
        '''
        pass

    def store_value(self,value,table_name,trait_name, trait_value,request):
        '''
        Objective: To store or update the value of the trait component in the database table.
        Input Parameter: value - Calculated value of the trait component
                         table_name - Database table in which the value is to be inserted/updated
                         trait_list - A list of Traits
                         value_list - A list of Values of the corresponding traits defined in the trait_list
        '''
        trait_obj=table_name.objects.filter(sid=request.user).update(**{self.trait_component:value})
        trait_name.append(self.trait_component)
        trait_value.append(value)
        return value

    def calc_overall_health(self,trait_value, traitWeightageList,request):
        '''
        Objective: To calculate the overall health of the seller.
        Input Parameter: value_list - A list of Values of the corresponding traits defined in the trait_list
        Return Value: overall_value_health - Overall health value of the seller
        '''
        numerator = [trait_value[i]*traitWeightageList[i] for i in range(len(trait_value))]
        overall_value_health = sum(numerator) / sum(traitWeightageList)
        print(numerator)
        print(traitWeightageList)
        print(overall_value_health)
        self.store_overall_value(TraitValueDetails,overall_value_health,request)
        #return overall_value_health

    def store_overall_value(self,TraitValueDetails ,overall_value_health,request):
        '''
        numerator = [trait_value[i]*traitWeightageList[i] for i in range(len(trait_value))]
        Objective: To store or update the overall health of the seller.
        Input Paramter: tabel_name - Database table in which the value is to be inserted/updated
                        overall_health - Overall health value of the seller
        '''
        TraitValueDetails.objects.filter(
                    sid=request.user
                    ).update(
                    overall_value_health = overall_value_health
                    )

class KycValue(Trait):
    '''
    Objective: A derived class of Trait which calculates the value of 'KYC' trait
    '''
    def calc_value(self,request):
        '''
        Objective: Calculates the values of KYC
        Return Value: value - Value of the KYC details of the seller.
        '''

        if SellerDetails.objects.filter(sid=request.user).exists():
            obj = SellerDetails.objects.get(sid=request.user)
            if obj.sKYC_flag == 'empty':
                    value = 0
            if obj.sKYC_flag == 'inprocess':
                value = 50
            elif obj.sKYC_flag == 'accepted':
                value = 100
            elif obj.sKYC_flag == 'rejected':
                value = 0
            #print(value)
            return value

    def returnTraitWeightage(self):
        return 2

    def saveRecommendation(self, value, recommendation_list,request):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_kycValue = "We recommend you to fill your KYC details."
                )
            recommendation_list.append("We recommend you to fill your KYC details.")
        elif value == 50:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_kycValue = "Your KYC verification is in process. We'll update you about the status"
                )
            recommendation_list.append("Your KYC verification is in process. We'll update you about the status")
        else:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_kycValue = "Your KYC details has been accepted"
                )
            recommendation_list.append("Your KYC details has been accepted")

class GstValue(Trait):
    '''
    Objective: A derived class of Trait which calculates the value of 'GST' trait
    '''
    def calc_value(self,request):
        '''
        Objective: Calculates the values of gst
        Return Value: value - Value of the GST details of the seller.
        '''
        if SellerDetails.objects.filter(sid=request.user).exists():
            #obj = SellerDetails.objects.get(sid=request.user)
            obj = SellerBusinessDetails.objects.get(sid = request.user)
            #print(obj.gst_no)
            if obj.gst_flag == 'empty':
                    value = 0
            if obj.gst_flag == 'inprocess':
                value = 50
            elif obj.gst_flag == 'accepted':
                value = 100
            elif obj.gst_flag == 'rejected':
                value = 0
            #print(value)
            return value

    def returnTraitWeightage(self):
        return 2

    def saveRecommendation(self, value, recommendation_list,request):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_gstValue = "We recommend you to fill your GST details."
                )
            recommendation_list.append("We recommend you to fill your GST details.")
        elif value == 50:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_gstValue = "Your GST verification is in process. We'll update you about the status."
                )
            recommendation_list.append("Your GST verification is in process. We'll update you about the status.")
        else:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_gstValue = "Your GST details has been accepted."
                )
            recommendation_list.append("Your GST details has been accepted.")

class CreditCardValue(Trait):
    '''
    Objective: A derived class of Trait which calculates the value of 'Credit card' trait
    '''
    def calc_value(self,request):
        '''
        Objective: Calculates the values of Credit card score
        Return Value: value - Value of the Credit card details of the seller.
        '''
        if SellerDetails.objects.filter(sid=request.user).exists():
            obj = SellerBusinessDetails.objects.get(sid=request.user)
            delta = obj.expiry_date - datetime.now().date()
            if delta < timedelta(days=20):
                value = 0
            else:
                value = 100
            return value

    def returnTraitWeightage(self):
        return 3

    def saveRecommendation(self, value, recommendation_list,request):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_creditCardValue = "Your Credit card is about to expire. Please update your Credit card details."
                )
            recommendation_list.append("Your Credit card is about to expire. Please update your Credit card details.")
        else:
            TraitValueDetails.objects.filter(
                ).update(
                recommendations_creditCardValue = "Your Credit card details are up to date."
                )
            recommendation_list.append("Your Credit card details are up to date.")
