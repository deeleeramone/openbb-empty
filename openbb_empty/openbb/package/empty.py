### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import Literal, Optional

from openbb_core.app.model.field import OpenBBField
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import exception_handler, validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated


class ROUTER_empty(Container):
    """/empty
    empty_function
    hello
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @exception_handler
    @validate
    def empty_function(
        self,
        provider: Annotated[
            Optional[Literal["empty"]],
            OpenBBField(
                description="The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: empty."
            ),
        ] = None,
        **kwargs
    ) -> OBBject:
        """An empty function using the Provider Interface.

        Parameters
        ----------
        provider : Optional[Literal['empty']]
            The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: empty.
        some_param : Dict[Any, Any]
            Some param (provider: empty)

        Returns
        -------
        OBBject
            results : Empty
                Serializable results.
            provider : Optional[Literal['empty']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra : Dict[str, Any]
                Extra info.

        Empty
        -----
        date : Optional[date]
            Date of the data. (provider: empty)
        title : Optional[str]
            Title of the data. (provider: empty)

        Examples
        --------
        >>> from openbb import obb
        >>> obb.empty.empty_function(provider='empty')
        >>> # Say Hello.
        >>> result = obb.empty.hello()
        """  # noqa: E501

        return self._run(
            "/empty/empty_function",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "empty.empty_function",
                        ("empty",),
                    )
                },
                standard_params={},
                extra_params=kwargs,
            )
        )

    @exception_handler
    @validate
    def hello(
        self,
    ) -> OBBject:
        """OpenBB Hello World."""  # noqa: E501

        return self._run("/empty/hello", **filter_inputs())
