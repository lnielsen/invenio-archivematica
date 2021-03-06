# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
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
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Admin views fot the table Archive."""

from flask_admin.contrib.sqla import ModelView

from invenio_archivematica.models import Archive


class ArchiveModelView(ModelView):
    """ModelView for the Archive table."""

    can_create = False
    can_edit = False
    can_delete = False
    can_view_details = True
    column_display_all_relations = True
    column_list = (
        'sip_id', 'sip.created', 'status', 'accession_id', 'archivematica_id'
    )
    column_labels = {
        'sip_id': 'ID of the SIP',
        'sip.created': 'Last update',
        'status': 'Status',
        'accession_id': 'AIP Accession ID',
        'archivematica_id': 'Archivematica ID'
    }
    page_size = 25


archive_adminview = dict(
    modelview=ArchiveModelView,
    model=Archive,
    name='Archive',
    category='Records')
