"""Domain Query Specifications for API Gateway Service Repositories."""

import abc
from typing import Any, Dict, List
from services.api_gateway.domain.models import GatewayRouteAggregate

class IGatewayRouteSpecification(abc.ABC):
    """Specification pattern interface for composable aggregate filtering."""
    @abc.abstractmethod
    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        pass

    def and_spec(self, other: "IGatewayRouteSpecification") -> "IGatewayRouteSpecification":
        return AndGatewayRouteSpecification(self, other)

    def or_spec(self, other: "IGatewayRouteSpecification") -> "IGatewayRouteSpecification":
        return OrGatewayRouteSpecification(self, other)

    def not_spec(self) -> "IGatewayRouteSpecification":
        return NotGatewayRouteSpecification(self)

class AndGatewayRouteSpecification(IGatewayRouteSpecification):
    def __init__(self, left: IGatewayRouteSpecification, right: IGatewayRouteSpecification) -> None:
        self.left = left
        self.right = right
    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        return self.left.is_satisfied_by(aggregate) and self.right.is_satisfied_by(aggregate)

class OrGatewayRouteSpecification(IGatewayRouteSpecification):
    def __init__(self, left: IGatewayRouteSpecification, right: IGatewayRouteSpecification) -> None:
        self.left = left
        self.right = right
    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        return self.left.is_satisfied_by(aggregate) or self.right.is_satisfied_by(aggregate)

class NotGatewayRouteSpecification(IGatewayRouteSpecification):
    def __init__(self, spec: IGatewayRouteSpecification) -> None:
        self.spec = spec
    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        return not self.spec.is_satisfied_by(aggregate)

class GatewayRouteSpecCriteria01(IGatewayRouteSpecification):
    """Specification criteria 01 filtering by domain attribute 1."""
    def __init__(self, target_value: str = "val_1", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_1"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria02(IGatewayRouteSpecification):
    """Specification criteria 02 filtering by domain attribute 2."""
    def __init__(self, target_value: str = "val_2", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_2"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria03(IGatewayRouteSpecification):
    """Specification criteria 03 filtering by domain attribute 3."""
    def __init__(self, target_value: str = "val_3", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_3"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria04(IGatewayRouteSpecification):
    """Specification criteria 04 filtering by domain attribute 4."""
    def __init__(self, target_value: str = "val_4", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_4"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria05(IGatewayRouteSpecification):
    """Specification criteria 05 filtering by domain attribute 5."""
    def __init__(self, target_value: str = "val_5", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_5"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria06(IGatewayRouteSpecification):
    """Specification criteria 06 filtering by domain attribute 6."""
    def __init__(self, target_value: str = "val_6", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_6"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria07(IGatewayRouteSpecification):
    """Specification criteria 07 filtering by domain attribute 7."""
    def __init__(self, target_value: str = "val_7", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_7"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria08(IGatewayRouteSpecification):
    """Specification criteria 08 filtering by domain attribute 8."""
    def __init__(self, target_value: str = "val_8", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_8"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria09(IGatewayRouteSpecification):
    """Specification criteria 09 filtering by domain attribute 9."""
    def __init__(self, target_value: str = "val_9", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_9"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria10(IGatewayRouteSpecification):
    """Specification criteria 10 filtering by domain attribute 10."""
    def __init__(self, target_value: str = "val_10", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_10"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria11(IGatewayRouteSpecification):
    """Specification criteria 11 filtering by domain attribute 11."""
    def __init__(self, target_value: str = "val_11", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_11"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria12(IGatewayRouteSpecification):
    """Specification criteria 12 filtering by domain attribute 12."""
    def __init__(self, target_value: str = "val_12", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_12"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria13(IGatewayRouteSpecification):
    """Specification criteria 13 filtering by domain attribute 13."""
    def __init__(self, target_value: str = "val_13", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_13"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria14(IGatewayRouteSpecification):
    """Specification criteria 14 filtering by domain attribute 14."""
    def __init__(self, target_value: str = "val_14", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_14"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria15(IGatewayRouteSpecification):
    """Specification criteria 15 filtering by domain attribute 15."""
    def __init__(self, target_value: str = "val_15", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_15"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria16(IGatewayRouteSpecification):
    """Specification criteria 16 filtering by domain attribute 16."""
    def __init__(self, target_value: str = "val_16", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_16"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria17(IGatewayRouteSpecification):
    """Specification criteria 17 filtering by domain attribute 17."""
    def __init__(self, target_value: str = "val_17", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_17"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria18(IGatewayRouteSpecification):
    """Specification criteria 18 filtering by domain attribute 18."""
    def __init__(self, target_value: str = "val_18", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_18"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria19(IGatewayRouteSpecification):
    """Specification criteria 19 filtering by domain attribute 19."""
    def __init__(self, target_value: str = "val_19", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_19"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria20(IGatewayRouteSpecification):
    """Specification criteria 20 filtering by domain attribute 20."""
    def __init__(self, target_value: str = "val_20", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_20"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria21(IGatewayRouteSpecification):
    """Specification criteria 21 filtering by domain attribute 21."""
    def __init__(self, target_value: str = "val_21", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_21"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria22(IGatewayRouteSpecification):
    """Specification criteria 22 filtering by domain attribute 22."""
    def __init__(self, target_value: str = "val_22", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_22"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria23(IGatewayRouteSpecification):
    """Specification criteria 23 filtering by domain attribute 23."""
    def __init__(self, target_value: str = "val_23", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_23"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria24(IGatewayRouteSpecification):
    """Specification criteria 24 filtering by domain attribute 24."""
    def __init__(self, target_value: str = "val_24", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_24"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria25(IGatewayRouteSpecification):
    """Specification criteria 25 filtering by domain attribute 25."""
    def __init__(self, target_value: str = "val_25", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_25"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria26(IGatewayRouteSpecification):
    """Specification criteria 26 filtering by domain attribute 26."""
    def __init__(self, target_value: str = "val_26", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_26"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria27(IGatewayRouteSpecification):
    """Specification criteria 27 filtering by domain attribute 27."""
    def __init__(self, target_value: str = "val_27", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_27"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria28(IGatewayRouteSpecification):
    """Specification criteria 28 filtering by domain attribute 28."""
    def __init__(self, target_value: str = "val_28", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_28"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria29(IGatewayRouteSpecification):
    """Specification criteria 29 filtering by domain attribute 29."""
    def __init__(self, target_value: str = "val_29", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_29"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria30(IGatewayRouteSpecification):
    """Specification criteria 30 filtering by domain attribute 30."""
    def __init__(self, target_value: str = "val_30", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_30"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria31(IGatewayRouteSpecification):
    """Specification criteria 31 filtering by domain attribute 31."""
    def __init__(self, target_value: str = "val_31", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_31"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria32(IGatewayRouteSpecification):
    """Specification criteria 32 filtering by domain attribute 32."""
    def __init__(self, target_value: str = "val_32", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_32"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria33(IGatewayRouteSpecification):
    """Specification criteria 33 filtering by domain attribute 33."""
    def __init__(self, target_value: str = "val_33", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_33"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria34(IGatewayRouteSpecification):
    """Specification criteria 34 filtering by domain attribute 34."""
    def __init__(self, target_value: str = "val_34", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_34"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria35(IGatewayRouteSpecification):
    """Specification criteria 35 filtering by domain attribute 35."""
    def __init__(self, target_value: str = "val_35", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_35"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria36(IGatewayRouteSpecification):
    """Specification criteria 36 filtering by domain attribute 36."""
    def __init__(self, target_value: str = "val_36", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_36"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria37(IGatewayRouteSpecification):
    """Specification criteria 37 filtering by domain attribute 37."""
    def __init__(self, target_value: str = "val_37", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_37"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria38(IGatewayRouteSpecification):
    """Specification criteria 38 filtering by domain attribute 38."""
    def __init__(self, target_value: str = "val_38", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_38"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria39(IGatewayRouteSpecification):
    """Specification criteria 39 filtering by domain attribute 39."""
    def __init__(self, target_value: str = "val_39", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_39"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria40(IGatewayRouteSpecification):
    """Specification criteria 40 filtering by domain attribute 40."""
    def __init__(self, target_value: str = "val_40", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_40"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria41(IGatewayRouteSpecification):
    """Specification criteria 41 filtering by domain attribute 41."""
    def __init__(self, target_value: str = "val_41", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_41"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria42(IGatewayRouteSpecification):
    """Specification criteria 42 filtering by domain attribute 42."""
    def __init__(self, target_value: str = "val_42", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_42"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria43(IGatewayRouteSpecification):
    """Specification criteria 43 filtering by domain attribute 43."""
    def __init__(self, target_value: str = "val_43", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_43"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)

class GatewayRouteSpecCriteria44(IGatewayRouteSpecification):
    """Specification criteria 44 filtering by domain attribute 44."""
    def __init__(self, target_value: str = "val_44", match_mode: str = "EXACT") -> None:
        self.target_value = target_value
        self.match_mode = match_mode
        self.field_key = "attr_spec_44"

    def is_satisfied_by(self, aggregate: GatewayRouteAggregate) -> bool:
        if aggregate.is_deleted:
            return False
        actual = aggregate.attributes.get(self.field_key)
        if actual is None:
            return True
        if self.match_mode == "EXACT":
            return str(actual) == self.target_value
        return self.target_value in str(actual)
