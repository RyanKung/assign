import ast

__all__ = [
    'gen_assign_checker_ast',
    'AssignTransformer'

]


def gen_assign_checker_ast(node):
    targets = [t.id for t in node.targets]
    obj_name = node.value.id

    return ast.If(
        test=ast.Call(
            func=ast.Name(id='hasattr', ctx=ast.Load()),
            args=[
                ast.Name(id=obj_name, ctx=ast.Load()),
                ast.Str(s='__assign__'),
            ],
            keywords=[],
            starargs=None,
            kwargs=None
        ),
        body=[
            ast.Assign(
                targets=[ast.Name(id=target, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id=obj_name, ctx=ast.Load()),
                        attr='__assign__',
                        ctx=ast.Load()
                    ),
                    args=[ast.Str(s=target)],
                    keywords=[],
                    starargs=None,
                    kwargs=None
                )
            )
            for target in targets],
        orelse=[]
    )


class AssignTransformer(ast.NodeTransformer):
    def generic_visit(self, node):
        ast.NodeTransformer.generic_visit(self, node)
        return node

    def visit_Assign(self, node):
        if not isinstance(node.value, ast.Name):
            return node
        new_node = gen_assign_checker_ast(node)
        ast.copy_location(new_node, node)
        ast.fix_missing_locations(new_node)
        return new_node
