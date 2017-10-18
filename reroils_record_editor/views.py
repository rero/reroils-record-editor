# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 RERO.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""reroils record editor."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, current_app, render_template

from .utils import get_schema

blueprint = Blueprint(
    'reroils_record_editor',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/editor'
)


@blueprint.route("/new")
def index():
    """Render a basic view."""
    from json import loads
    from pkg_resources import resource_string

    options = current_app.config['REROILS_RECORD_EDITOR_FORM_OPTIONS']
    options_in_bytes = resource_string(*options)

    return render_template(
        "reroils_record_editor/index.html",
        form=loads(options_in_bytes.decode('utf8')),
        model={},
        schema=get_schema(
            current_app.config['REROILS_RECORD_EDITOR_JSONSCHEMA']
        )
    )
