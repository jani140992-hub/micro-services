"""Domain Query Specifications for User Profile Service Repositories."""

import abc
from typing import Any, Dict, List
from services.user_service.domain.models import UserProfileAggregate

class IUserProfileSpecification(abc.ABC):
    """Specification pattern interface for composable aggregate filtering."""
    @abc.abstractmethod
    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        pass

    def and_spec(self, other: "IUserProfileSpecification") -> "IUserProfileSpecification":
        return AndUserProfileSpecification(self, other)

    def or_spec(self, other: "IUserProfileSpecification") -> "IUserProfileSpecification":
        return OrUserProfileSpecification(self, other)

    def not_spec(self) -> "IUserProfileSpecification":
        return NotUserProfileSpecification(self)

class AndUserProfileSpecification(IUserProfileSpecification):
    def __init__(self, left: IUserProfileSpecification, right: IUserProfileSpecification) -> None:
        self.left = left
        self.right = right
    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        return self.left.is_satisfied_by(aggregate) and self.right.is_satisfied_by(aggregate)

class OrUserProfileSpecification(IUserProfileSpecification):
    def __init__(self, left: IUserProfileSpecification, right: IUserProfileSpecification) -> None:
        self.left = left
        self.right = right
    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        return self.left.is_satisfied_by(aggregate) or self.right.is_satisfied_by(aggregate)

class NotUserProfileSpecification(IUserProfileSpecification):
    def __init__(self, spec: IUserProfileSpecification) -> None:
        self.spec = spec
    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        return not self.spec.is_satisfied_by(aggregate)

class UserProfileSpecCriteria01(IUserProfileSpecification):
    """Specification criteria 01 filtering by domain attribute 1."""
    def __init__(self, target_value: str = "val_1", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_1"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria02(IUserProfileSpecification):
    """Specification criteria 02 filtering by domain attribute 2."""
    def __init__(self, target_value: str = "val_2", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_2"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria03(IUserProfileSpecification):
    """Specification criteria 03 filtering by domain attribute 3."""
    def __init__(self, target_value: str = "val_3", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_3"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria04(IUserProfileSpecification):
    """Specification criteria 04 filtering by domain attribute 4."""
    def __init__(self, target_value: str = "val_4", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_4"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria05(IUserProfileSpecification):
    """Specification criteria 05 filtering by domain attribute 5."""
    def __init__(self, target_value: str = "val_5", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_5"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria06(IUserProfileSpecification):
    """Specification criteria 06 filtering by domain attribute 6."""
    def __init__(self, target_value: str = "val_6", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_6"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria07(IUserProfileSpecification):
    """Specification criteria 07 filtering by domain attribute 7."""
    def __init__(self, target_value: str = "val_7", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_7"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria08(IUserProfileSpecification):
    """Specification criteria 08 filtering by domain attribute 8."""
    def __init__(self, target_value: str = "val_8", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_8"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria09(IUserProfileSpecification):
    """Specification criteria 09 filtering by domain attribute 9."""
    def __init__(self, target_value: str = "val_9", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_9"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria10(IUserProfileSpecification):
    """Specification criteria 10 filtering by domain attribute 10."""
    def __init__(self, target_value: str = "val_10", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_10"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria11(IUserProfileSpecification):
    """Specification criteria 11 filtering by domain attribute 11."""
    def __init__(self, target_value: str = "val_11", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_11"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria12(IUserProfileSpecification):
    """Specification criteria 12 filtering by domain attribute 12."""
    def __init__(self, target_value: str = "val_12", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_12"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria13(IUserProfileSpecification):
    """Specification criteria 13 filtering by domain attribute 13."""
    def __init__(self, target_value: str = "val_13", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_13"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria14(IUserProfileSpecification):
    """Specification criteria 14 filtering by domain attribute 14."""
    def __init__(self, target_value: str = "val_14", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_14"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria15(IUserProfileSpecification):
    """Specification criteria 15 filtering by domain attribute 15."""
    def __init__(self, target_value: str = "val_15", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_15"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria16(IUserProfileSpecification):
    """Specification criteria 16 filtering by domain attribute 16."""
    def __init__(self, target_value: str = "val_16", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_16"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria17(IUserProfileSpecification):
    """Specification criteria 17 filtering by domain attribute 17."""
    def __init__(self, target_value: str = "val_17", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_17"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria18(IUserProfileSpecification):
    """Specification criteria 18 filtering by domain attribute 18."""
    def __init__(self, target_value: str = "val_18", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_18"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria19(IUserProfileSpecification):
    """Specification criteria 19 filtering by domain attribute 19."""
    def __init__(self, target_value: str = "val_19", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_19"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria20(IUserProfileSpecification):
    """Specification criteria 20 filtering by domain attribute 20."""
    def __init__(self, target_value: str = "val_20", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_20"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria21(IUserProfileSpecification):
    """Specification criteria 21 filtering by domain attribute 21."""
    def __init__(self, target_value: str = "val_21", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_21"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria22(IUserProfileSpecification):
    """Specification criteria 22 filtering by domain attribute 22."""
    def __init__(self, target_value: str = "val_22", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_22"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria23(IUserProfileSpecification):
    """Specification criteria 23 filtering by domain attribute 23."""
    def __init__(self, target_value: str = "val_23", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_23"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria24(IUserProfileSpecification):
    """Specification criteria 24 filtering by domain attribute 24."""
    def __init__(self, target_value: str = "val_24", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_24"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria25(IUserProfileSpecification):
    """Specification criteria 25 filtering by domain attribute 25."""
    def __init__(self, target_value: str = "val_25", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_25"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria26(IUserProfileSpecification):
    """Specification criteria 26 filtering by domain attribute 26."""
    def __init__(self, target_value: str = "val_26", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_26"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria27(IUserProfileSpecification):
    """Specification criteria 27 filtering by domain attribute 27."""
    def __init__(self, target_value: str = "val_27", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_27"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria28(IUserProfileSpecification):
    """Specification criteria 28 filtering by domain attribute 28."""
    def __init__(self, target_value: str = "val_28", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_28"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria29(IUserProfileSpecification):
    """Specification criteria 29 filtering by domain attribute 29."""
    def __init__(self, target_value: str = "val_29", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_29"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria30(IUserProfileSpecification):
    """Specification criteria 30 filtering by domain attribute 30."""
    def __init__(self, target_value: str = "val_30", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_30"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria31(IUserProfileSpecification):
    """Specification criteria 31 filtering by domain attribute 31."""
    def __init__(self, target_value: str = "val_31", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_31"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria32(IUserProfileSpecification):
    """Specification criteria 32 filtering by domain attribute 32."""
    def __init__(self, target_value: str = "val_32", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_32"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria33(IUserProfileSpecification):
    """Specification criteria 33 filtering by domain attribute 33."""
    def __init__(self, target_value: str = "val_33", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_33"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria34(IUserProfileSpecification):
    """Specification criteria 34 filtering by domain attribute 34."""
    def __init__(self, target_value: str = "val_34", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_34"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria35(IUserProfileSpecification):
    """Specification criteria 35 filtering by domain attribute 35."""
    def __init__(self, target_value: str = "val_35", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_35"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria36(IUserProfileSpecification):
    """Specification criteria 36 filtering by domain attribute 36."""
    def __init__(self, target_value: str = "val_36", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_36"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria37(IUserProfileSpecification):
    """Specification criteria 37 filtering by domain attribute 37."""
    def __init__(self, target_value: str = "val_37", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_37"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria38(IUserProfileSpecification):
    """Specification criteria 38 filtering by domain attribute 38."""
    def __init__(self, target_value: str = "val_38", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_38"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria39(IUserProfileSpecification):
    """Specification criteria 39 filtering by domain attribute 39."""
    def __init__(self, target_value: str = "val_39", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_39"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria40(IUserProfileSpecification):
    """Specification criteria 40 filtering by domain attribute 40."""
    def __init__(self, target_value: str = "val_40", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_40"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria41(IUserProfileSpecification):
    """Specification criteria 41 filtering by domain attribute 41."""
    def __init__(self, target_value: str = "val_41", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_41"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria42(IUserProfileSpecification):
    """Specification criteria 42 filtering by domain attribute 42."""
    def __init__(self, target_value: str = "val_42", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_42"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria43(IUserProfileSpecification):
    """Specification criteria 43 filtering by domain attribute 43."""
    def __init__(self, target_value: str = "val_43", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_43"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class UserProfileSpecCriteria44(IUserProfileSpecification):
    """Specification criteria 44 filtering by domain attribute 44."""
    def __init__(self, target_value: str = "val_44", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_44"

    def is_satisfied_by(self, aggregate: UserProfileAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)
