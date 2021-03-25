# Copyright (C) 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
"""
This file demonstrates how you can extend an existing frePPLe model with
custom attributes.
"""

# Use the function "_" for all strings that can be translated.
from django.utils.translation import gettext_lazy as _
from freppledb.boot import registerAttribute

registerAttribute(
    "freppledb.input.models.Item",  # Class we are extending
    [
        (
            "attribute_1",  # Field name in the database
            _("first attribute"),  # Human readable label of the field
            "number",  # Type of the field.
            True,  # Is the field editable?
            True,  # Should the field be visible by default?
        )
    ],
)
