class MyCloudException(Exception): ...


class ResourceException(MyCloudException): ...


class ResourceAlreadyExistsException(ResourceException): ...


class ResourceNotFoundException(ResourceException): ...
