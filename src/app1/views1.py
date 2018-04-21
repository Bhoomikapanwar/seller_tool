from django.shortcuts import render
from dashboard.models import *
from django.db.models import Count, F, Sum
from abc import ABC, abstractmethod
import re

class Trait(ABC):
    '''
        Objective: An abstract class which calculates the value of the trait and stores it in the database.
    '''
    traitWeightageList = []
    def __init__(self, trait_cmp):
        '''
        Objective: A constructor which initializes the trait component variable.
        Input Parameter: trait_cmp - Trait Component
        Return Value: Returns an object of the called class
        '''
        self.trait_component = trait_cmp

    def template_method(self, trait_name, trait_value, recommendation_list):
        '''
        Objective: Template method defines an algorithm's skeleton in the Trait base class
                    and let subclasses redefine certain steps of the algorithm.
        Input Parameter: trait_list - A list of Traits
                         value_list - A list of Values of the corresponding traits defined in the trait_list
        '''
        table_name = self.find_table()
        self.store_sid(table_name)
        value = self.calc_value()
        traitWeightage = self.returnTraitWeightage()
        Trait.traitWeightageList.append(traitWeightage)
        self.saveRecommendation(value, recommendation_list)
        self.store_value(value, table_name, trait_name, trait_value)
        overall_value_healthue = self.calc_overall_performance(trait_value,Trait.traitWeightageList)
        self.store_overall_value(TraitValueDetails,overall_value_healthue)

    def find_table(self):
        '''
        Objective: To find the database table which contains the trait_component field .
        Return Value: Returns the database table name
        '''
        for cls in Base_TraitValueDetails.__subclasses__():
            field=cls._meta.get_field(self.trait_component)
            if field:
                return cls

    def store_sid(self,table_name):
        '''
        Objective: To check and then store the sid of seller in the table_name which contains trait_component.
        Input Parameter: table_name - Table which contains trait_component
        '''
        check=table_name.objects.filter(sid=request.user).exists()
        if check==False:
            s=SellerDetails.objects.get(sid=request.user)
            save_sid=table_name(sid=s)
            save_sid.save()

    @abstractmethod
    def calc_value(self):
        '''
        Objective: An abstract method which calculates the value of trait_component.
        Return Value: Calculated Value of the trait.
        '''
        pass

    def store_value(self,value,table_name,trait_name, trait_value):
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

    def calc_overall_performance(self,trait_value, traitWeightageList):
        '''
        Objective: To calculate the overall performance of the seller.
        Input Parameter: value_list - A list of Values of the corresponding traits defined in the trait_list
        Return Value: overall_value_health - Overall performance value of the seller
        '''
        overall_value_health = sum(numerator) / sum(traitWeightageList)
        return overall_value_health

    def store_overall_value(self,TraitValueDetails ,overall_value_healthue):
        '''
        numerator = [trait_value[i]*traitWeightageList[i] for i in range(len(trait_value))]
        Objective: To store or update the overall performance of the seller.
        Input Paramter: tabel_name - Database table in which the value is to be inserted/updated
                        overall_performance - Overall performance value of the seller
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
    def calc_value(self):
        '''
        Objective: Calculates the values of KYC
        Return Value: value - Value of the KYC details of the seller.
        '''
            obj = SellerDetails.objects.get(sid=request.user)
            if SellerDetails.objects.filter(sid=request.user).exists():
            if not obj.sKYC:
                value = 0
            else:
                if obj.sKYC_flag == 'inprocess':
                    value = 50
                elif obj.sKYC_flag == 'accepted':
                    value = 100
                elif obj.sKYC_flag == 'rejected':
                    value = 0
            return value

    def returnTraitWeightage(self):
        return 2

    def saveRecommendation(self, value, recommendation_list):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_kycValue = "recommendation 1"
                )
            recommendation_list.append("recommendation 1")
        elif value == 50:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_lateShipmentRate = "recommendation 2"
                )
            recommendation_list.append("recommendation 2")
        else:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_lateShipmentRate = "recommendation 3"
                )
            recommendation_list.append("recommendation 3")

class GstValue(Trait):
    '''
    Objective: A derived class of Trait which calculates the value of 'GST' trait
    '''
    def calc_value(self):
        '''
        Objective: Calculates the values of gst
        Return Value: value - Value of the GST details of the seller.
        '''
        if SellerDetails.objects.filter(sid=request.user).exists():
            obj = SellerDetails.objects.get(sid=request.user)
            if not obj.gst_no:
                value = 0
            else:
                if obj.gst_flag == 'inprocess':
                    value = 50
                elif obj.gst_flag == 'accepted':
                    value = 100
                elif obj.gst_flag == 'rejected':
                    value = 0
            return value

    def returnTraitWeightage(self):
        return 1

    def saveRecommendation(self, value, recommendation_list):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_kycValue = "recommendation 1"
                )
            recommendation_list.append("recommendation 1")
        elif value == 50:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_lateShipmentRate = "recommendation 2"
                )
            recommendation_list.append("recommendation 2")
        else:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_lateShipmentRate = "recommendation 3"
                )
            recommendation_list.append("recommendation 3")

class CreditCardValue(Trait):
    '''
    Objective: A derived class of Trait which calculates the value of 'Credit card' trait
    '''
    def calc_value(self):
        '''
        Objective: Calculates the values of Credit card score
        Return Value: value - Value of the Credit card details of the seller.
        '''
        if SellerDetails.objects.filter(sid=request.user).exists():
            obj = SellerDetails.objects.get(sid=request.user)
            delta = obj.expiry_date - datetime.now().date()
            if delta < timedelta(days=20):
                value = 0
            else:
                value = 100
            return value

    def returnTraitWeightage(self):
        return 2

    def saveRecommendation(self, value, recommendation_list):
        if value == 0:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_creditCardValue = "recommendation 1"
                )
            recommendation_list.append("recommendation 1")
        '''elif value == 50:
            TraitValueDetails.objects.filter(
                sid=request.user
                ).update(
                recommendations_creditCardValue = "recommendation 2"
                )
            recommendation_list.append("recommendation 2")'''
        else:
            TraitValueDetails.objects.filter(
                ).update(
                recommendations_creditCardValue = "recommendation 3"
                )
            recommendation_list.append("recommendation 3")

def main(request):
    sid=request.user
    trait_name = []
    trait_value = []
    recommendation_list = []
    for cls in Trait.__subclasses__():

        class_name = cls.__name__
        trait_component = re.sub( '(?<!^)(?=[A-Z])', '_', class_name ).lower()
        obj = cls(trait_component)
        obj.template_method(trait_name, trait_value, recommendation_list)

    recommendation_trait_list = zip(trait_name, trait_value, recommendation_list)
    return render(request,'dashboard.html',{'recommendation_trait_list':recommendation_trait_list})

if __name__ == '__main__':
    main(request)
