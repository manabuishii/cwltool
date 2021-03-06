# Stubs for galaxy.tools.deps.brew_exts (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

WHITESPACE_PATTERN = ...  # type: Any
DESCRIPTION = ...  # type: str
DEFAULT_HOMEBREW_ROOT = ...  # type: str
NO_BREW_ERROR_MESSAGE = ...  # type: str
CANNOT_DETERMINE_TAP_ERROR_MESSAGE = ...  # type: str
VERBOSE = ...  # type: bool
RELAXED = ...  # type: bool
BREW_ARGS = ...  # type: Any

class BrewContext:
    homebrew_prefix = ...  # type: Any
    homebrew_cellar = ...  # type: Any
    def __init__(self, args: Optional[Any] = ...) -> None: ...

class RecipeContext:
    @staticmethod
    def from_args(args, brew_context: Optional[Any] = ...): ...
    recipe = ...  # type: Any
    version = ...  # type: Any
    brew_context = ...  # type: Any
    def __init__(self, recipe, version, brew_context: Optional[Any] = ...) -> None: ...
    @property
    def cellar_path(self): ...
    @property
    def tap_path(self): ...

def main(): ...

class CommandLineException(Exception):
    command = ...  # type: Any
    stdout = ...  # type: Any
    stderr = ...  # type: Any
    message = ...  # type: Any
    def __init__(self, command, stdout, stderr) -> None: ...

def versioned_install(recipe_context, package: Optional[Any] = ..., version: Optional[Any] = ..., installed_deps: Any = ...): ...
def commit_for_version(recipe_context, package, version): ...
def print_versioned_deps(recipe_context, recipe, version): ...
def load_versioned_deps(cellar_path, relaxed: Optional[Any] = ...): ...
def unversioned_install(package): ...
def attempt_unlink_all(package, deps): ...
def attempt_unlink(package): ...
def brew_execute(args, env: Optional[Any] = ...): ...
def build_env_statements_from_recipe_context(recipe_context, **kwds): ...
def build_env_statements(cellar_root, cellar_path, relaxed: Optional[Any] = ..., custom_only: bool = ...): ...
def build_env_actions(deps, cellar_root, cellar_path, relaxed: Optional[Any] = ..., custom_only: bool = ...): ...

class EnvAction:
    variable = ...  # type: Any
    action = ...  # type: Any
    value = ...  # type: Any
    def __init__(self, keg_root, action_description) -> None: ...
    @staticmethod
    def build_env(env_actions): ...
    def modify_environ(self, environ): ...
    def to_statements(self): ...

def brew_head_at_version(recipe_context, package, version): ...
def brew_head_at_commit(commit, tap_path): ...
def git_execute(args): ...
def execute(cmds, env: Optional[Any] = ...): ...
def brew_deps(package): ...
def brew_info(recipe): ...
def extended_brew_info(recipe): ...
def brew_versions_info(package, tap_path): ...
def recipe_cellar_path(cellar_path, recipe, version): ...
def ensure_brew_on_path(args): ...
def which(file): ...
