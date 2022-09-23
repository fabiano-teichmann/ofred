from flask import render_template, g, redirect
from flask_appbuilder import ModelView, action
from flask_appbuilder.models.filters import BaseFilter
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy import or_

from app.models import Domains, Applications, Events
from publisher.publisher import send_event_log
from . import appbuilder, db


class CustomAdminFilter(BaseFilter):
    """
    User defined filter
    Purpose: if user is not registered (in public domain), all records are returned
             if user is registered but not admin, only records created or changed by
             them are returned
             if user has admin permission, all records are returned
    """

    def apply(self, query, value):
        role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
        if g.user.is_anonymous:
            return query
        if not role_admin in g.user.roles:
            return query.filter(or_(Domains.created_by == g.user,
                                    Domains.changed_by == g.user))
        return query


class ApplicationsModelView(ModelView):
    @action("myaction", "Do something on this record", "Do you really want to?", "fa-rocket")
    def myaction(self, item):
        """
            do something with the item record
        """

        return redirect(self.get_redirect())

    datamodel = SQLAInterface(Applications)
    label_columns = {"applications": "Applications"}
    list_columns = ["name", "description"]
    edit_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    add_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    show_fieldsets = [
        (
            "Applications",
            {"fields": ["name", "description", "created_by", "created_on",
                        "changed_by", "changed_on"]}
        )
    ]


class DomainsModelView(ModelView):
    datamodel = SQLAInterface(Domains)
    label_columns = {"domains": "Domains"}
    list_columns = ["name", "description"]
    edit_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    add_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    show_fieldsets = [
        (
            "Domains",
            {"fields": ["name", "description", "created_by", "created_on",
                        "changed_by", "changed_on"]}
        )
    ]


class EventsModelView(ModelView):
    datamodel = SQLAInterface(Events)
    label_columns = {"events": "Events"}
    list_columns = [
        "event_name", "req_path", "description", "application_tbl", "domain_tbl", "fields_pii_req_body"]

    edit_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    add_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]

    show_fieldsets = [
        (
            "Events",
            {"fields": list_columns, "expanded": False}
        )
    ]

    def post_add(self, item):
        send_event_log(item)

    def pre_update(self, item):
        send_event_log(item)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(
    DomainsModelView,
    "Domains",
    icon="fa fa-briefcase",
    category="Domain",
    category_icon="fa fa-briefcase"
)
appbuilder.add_view(
    ApplicationsModelView,
    "Applications",
    icon="fa-server",
    category="Applications",
    category_icon="fa-server"
)
appbuilder.add_view(
    EventsModelView,
    "Events",
    icon="fa fa-file-code-o",
    category="Events",
    category_icon="fa fa-file-code-o"
)
