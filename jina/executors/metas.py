"""The default meta config that all executors follow, they can be overrided by the YAML config

Any executor inherited from :class:`BaseExecutor` always has the following **meta** fields:

    .. confval:: is_trained

        indicates if the executor is trained or not, if not then methods decorated by :func:`@required_train`
        can not be executed.

        :type: bool
        :default: ``False``

    .. confval:: is_updated

        indicates if the executor is updated or changed since last save, if not then :func:`save` will do nothing.
        A forced save is possible to use :func:`touch` before :func:`save`

        :type: bool
        :default: ``False``

    .. confval:: batch_size

        the size of each batch, methods decorated by :func:`@batching` will respect this. useful when incoming data is
        too large to fit into (GPU) memory.

        :type: int
        :default: ``None``

    .. confval:: workspace

        the working directory, for dumping and loading serialized executor.

        :type: str
        :default: environment variable :confval:`JINA_EXECUTOR_WORKDIR`, if not set then using current working dir, aka ``cwd``.

    .. confval:: name

        the name of the executor.

        :type: str
        :default: class name plus a random string

    .. confval:: on_gpu

        indicates if the executor is running on GPU.

        :type: bool
        :default: ``False``


    .. confval:: py_modules

        the external python module paths. it is useful when you want to load external python modules
        using :func:`BaseExecutor.load_config` from a YAML file. If a relative path is given then the root path is set to
        the path of the current YAML file.

        :type: str/List[str]
        :default: ``None``

    .. confval:: replica_id

        the integer index used for distinguish each replica of this executor, useful in :attr:`replica_workspace`

        :type: int
        :default: 0

    .. confval:: separated_workspace

        whether to isolate the data of the replicas of this executor. If ``True``, then each replica works in its own
        workspace specified in :attr:`replica_workspace`

        :type: bool
        :default: ``False``
        
    .. confval:: replica_workspace

        the workspace of each replica, useful when :attr:`separated_workspace` is set to True. All data and IO operations
        related to this replica will be conducted under this workspace. It is often set as the sub-directory of :attr:`workspace`.

        :type: str
        :default: ``{workspace}/{name}-{replica_id}``


    .. warning::
        ``name`` and ``workspace`` must be set if you want to serialize/deserialize this executor.



    These **meta** fields can be accessed via `self.is_trained` or loaded from a YAML config via :func:`load_config`:

    .. highlight:: yaml
    .. code-block:: yaml

        !MyAwesomeExecutor
        with:
          ...
        metas:
          name: my_transformer  # a customized name
          is_trained: true  # indicate the model has been trained
          workspace: ./  # path for serialize/deserialize

.. note::
    The overwrite priority is:

    metas defined in YAML > class attribute > metas.defaults

"""

import os

defaults = {
    'is_trained': False,
    'is_updated': False,
    'batch_size': None,
    'workspace': os.environ.get('JINA_EXECUTOR_WORKDIR', os.getcwd()),
    'name': None,
    'on_gpu': False,
    'warn_unnamed': os.environ.get('JINA_WARN_UNNAMED', False),
    'max_snapshot': 0,  # depreciated
    'py_modules': None,
    'replica_id': 0,
    'separated_workspace': False,
    'replica_workspace': '{workspace}/{name}-{replica_id}',
}