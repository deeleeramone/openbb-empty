### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /empty

Extensions:
    - empty@0.0.1

    - empty@0.0.1    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def empty(self):
        # pylint: disable=import-outside-toplevel
        from . import empty

        return empty.ROUTER_empty(command_runner=self._command_runner)
