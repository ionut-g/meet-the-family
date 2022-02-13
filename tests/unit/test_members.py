from multiprocessing.sharedctypes import Value
from unittest import TestCase
from family_tree.member import Member, Gender


class TestMember(TestCase):
    def setUp(self):
        self.member = Member(1, "Zim", Gender.MALE)

    def test_initialization(self):
        #check instance
        self.assertEqual(isinstance(self.member, Member), True)

        #check properties
        self.assertEqual(self.member.id, 1)
        self.assertEqual(self.member.name, "Zim")
        self.assertEqual(self.member.gender, Gender.MALE)
        self.assertEqual(self.member.mother, None)
        self.assertEqual(self.member.father, None)
        self.assertEqual(self.member.spouse, None)
        self.assertEqual(self.member.children, [])

        #edge case for gender 
        self.assertRaises(ValueError, Member, 2, "SomeOtherPerson","Queen")

    def test_set_mother(self):
        mother_demo_a = "mother_demo_a"
        mother_demo_b = Member(2,"MOtherDemoB", Gender.MALE)
        mother_demo_c = Member(3, "Mom", Gender.FEMALE)
        #error case
        self.assertRaises(ValueError, self.member.set_mother,mother_demo_a)
        self.assertRaises(ValueError, self.member.set_mother,mother_demo_b)
        #success case
        self.member.set_mother(mother_demo_c)
        self.assertEqual(self.member.mother.name, "Mom")
        self.assertEqual(self.member.mother.gender, Gender.FEMALE)

    def test_set_father(self):
        father_demo_a = "father_demo_a"
        father_demo_b = Member(2,"FatherDemoB", Gender.FEMALE)
        father_demo_c = Member(3, "Dad", Gender.MALE)
        #error case
        self.assertRaises(ValueError, self.member.set_father,father_demo_a)
        self.assertRaises(ValueError, self.member.set_father,father_demo_b)
        #success case
        self.member.set_father(father_demo_c)
        self.assertEqual(self.member.father.name, "Dad")
        self.assertEqual(self.member.father.gender, Gender.MALE)

    def test_set_spouse(self):
        spouse_demo_a = "spouse_demo_a"
        spouse_demo_b = Member(2,"SpouseDemoB", Gender.MALE)
        spouse_demo_c = Member(3, "wife", Gender.FEMALE)
        #error case
        self.assertRaises(ValueError, self.member.set_spouse,spouse_demo_a)
        self.assertRaises(ValueError, self.member.set_spouse,spouse_demo_b)
        #success case
        self.member.set_spouse(spouse_demo_c)
        self.assertEqual(self.member.spouse.name, "wife")
        self.assertEqual(self.member.spouse.gender, Gender.FEMALE)


    def test_add_child(self):
        child_demo_a = "child_demo_a"
        child_demo_b = Member(4,"Daughter", Gender.FEMALE)

        #error cases:
        self.member.add_child(child_demo_b)
        self.assertRaises(ValueError, self.member.add_child, child_demo_a)  
        self.assertEqual(len(self.member.children),1)
        self.assertEqual(self.member.children[0].name, "Daughter")
        self.assertEqual(self.member.children[0].gender, Gender.FEMALE)