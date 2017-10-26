import ast
from assign.transformer import AssignTransformer

__all__ = [
    'patch_node_ast',
    'patch_code_ast',
    'patch_file_ast',
    'patch_module_ast',
    'patch_module'
]


def patch_node_ast(node, trans=AssignTransformer):
    trans = trans()
    new_node = trans.visit(node)
    ast.fix_missing_locations(new_node)
    return new_node


def patch_code_ast(code_str, trans=AssignTransformer):
    code_ast = ast.parse(code_str)
    return patch_node_ast(code_ast, trans)


def patch_file_ast(filename, trans=AssignTransformer):
    with open(filename, "r") as f:
        code_str = ''.join(f.readlines())
        return patch_code_ast(code_str, trans)


def patch_module_ast(module, trans=AssignTransformer):
    if not hasattr(module, '__file__'):
        return module
    filename = module.__file__.replace('.pyc', '.py')
    return patch_file_ast(filename, trans)


def patch_module(module, trans=AssignTransformer):
    patched_ast = patch_module_ast(module)
    patched_code = compile(patched_ast, module.__name__, "exec")
    exec(patched_code, module.__dict__)
