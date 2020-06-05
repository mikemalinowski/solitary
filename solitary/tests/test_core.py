import unittest
import solitary


# --------------------------------------------------------------------------------------------------
@solitary.singleton
class SimpleSolitary(object):
    pass


# --------------------------------------------------------------------------------------------------
@solitary.singleton
class SimpleSolitaryWithArgs(object):
    def __init__(self, a, b):
        self.value = a + b


# --------------------------------------------------------------------------------------------------
class TestSolitary(unittest.TestCase):

    # ----------------------------------------------------------------------------------------------
    def test_instancing_two_solitary_classes(self):
        # -- Clean any pre-existing singletons
        solitary.flush()

        a = SimpleSolitary()
        b = SimpleSolitary()

        self.assertEqual(
            a,
            b,
        )

    # ----------------------------------------------------------------------------------------------
    def test_instancing_two_solitary_classes_wtih_args(self):
        a = SimpleSolitaryWithArgs(5, 5)
        b = SimpleSolitaryWithArgs(0, 0)

        self.assertEqual(
            a.value,
            10,
        )

        self.assertEqual(
            b.value,
            10,
        )

    # ----------------------------------------------------------------------------------------------
    def test_can_flush_single_class(self):

        # -- Create two classes of one type, and one class of another
        cls_a_v1 = SimpleSolitary()
        cls_a_v2 = SimpleSolitary()
        cls_b_v1 = SimpleSolitaryWithArgs(0, 0)

        # -- Flush the cls_a types
        solitary.flush(SimpleSolitary)

        # -- Now we need to check that cls_b type is in the
        # - cache still, so attempt to instance another
        cls_b_v2 = SimpleSolitaryWithArgs(0, 0)

        self.assertEqual(
            cls_b_v1,
            cls_b_v2,
        )

    # ----------------------------------------------------------------------------------------------
    def test_can_flush_all_classes(self):

        # -- Create two classes of one type, and one class of another
        cls_a_v1 = SimpleSolitary()
        cls_b_v1 = SimpleSolitaryWithArgs(0, 0)

        solitary.flush()

        # -- Create two new classes, these should now be unique
        cls_a_v2 = SimpleSolitary()
        cls_b_v2 = SimpleSolitaryWithArgs(0, 0)

        self.assertNotEqual(
            cls_a_v1,
            cls_a_v2,
        )

        self.assertNotEqual(
            cls_b_v1,
            cls_b_v2,
        )
