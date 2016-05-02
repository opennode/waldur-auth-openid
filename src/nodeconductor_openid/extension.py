from __future__ import unicode_literals

from nodeconductor.core import NodeConductorExtension


class NodeConductorOpenIDExtension(NodeConductorExtension):

    @staticmethod
    def django_app():
        return 'nodeconductor_openid'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

