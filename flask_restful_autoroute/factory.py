from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger_2 import Api as SwaggerApi, Resource as SwaggerResource

import reflections


def _blueprint(endpoint, url_prefix):
    return Blueprint(endpoint, __name__, url_prefix=url_prefix)


def _resource(target_package):
    resources = set()

    for loader, name in reflections.reflect(target_package, reflections.module_extractor):
        module_ = loader.find_module(name).load_module(name)
        for resource in module_.Resource.__subclasses__():
            resources.add(resource)

    return resources


def flask_restful_factory(endpoint, target_package, url_prefix=''):
    """
    :type endpoint: str
    :type target_package: package
    :type url_prefix: str

    :rtype: Blueprint
    """
    bp = _blueprint(endpoint, url_prefix)
    api = Api(bp)

    resources = _resource(target_package)
    SwaggerResource in resources and resources.remove(SwaggerResource)
    # flask-restful-swagger-2's Resource extends flask-restful's Resource

    for resource in resources:
        api.add_resource(resource, resource.uri)

    return bp


def flask_restful_swagger_factory(endpoint, target_package, url_prefix='', api_spec_url='/api/swagger', api_version='1.0', title='', desc=''):
    bp = _blueprint(endpoint, url_prefix)
    # api = Api(bp)
    api = SwaggerApi(bp, api_spec_url=api_spec_url, api_version=api_version, title=title, description=desc)

    resources = _resource(target_package)

    for resource in resources:
        api.add_resource(resource, resource.uri)

    return bp
