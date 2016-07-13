
import factory
from factory.django import DjangoModelFactory

from student.tests.factories import UserFactory

from biz.djangoapps.ga_contract_operation.models import ContractTaskHistory, ContractTaskTarget, StudentRegisterTaskTarget


class ContractTaskHistoryFactory(DjangoModelFactory):
    """Factory for the ContractTaskHistory model"""
    FACTORY_FOR = ContractTaskHistory

    requester = factory.SubFactory(UserFactory)


class ContractTaskTargetFactory(DjangoModelFactory):
    """Factory for the ContractTaskTarget model"""
    FACTORY_FOR = ContractTaskTarget


class StudentRegisterTaskTargetFactory(DjangoModelFactory):
    """Factory for the StudentRegisterTaskTarget model"""
    FACTORY_FOR = StudentRegisterTaskTarget
