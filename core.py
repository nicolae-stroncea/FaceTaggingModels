class Mixin:
    """Utility Base Class for SQLAlchemy Models. 
    
    Adds `to_dict()` to easily serialize objects to dictionaries.
    """

    def to_dict(self) -> dict:
        d_out = dict((key, val) for key, val in self.__dict__.items() if (not isinstance(val, bytes)))
        d_out.pop("_sa_instance_state", None)
        d_out["_id"] = d_out.pop("id", None)  # rename id key to interface with response
        return d_out


