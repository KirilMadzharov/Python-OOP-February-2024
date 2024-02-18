"""
Local, Global and Built-In Namespace
"""

"What is a Name spase?"

# A mapping from names to objects

# ▪ Examples:
# ▪ Built-in names, for example, the abs()function
# ▪ Global names in a module
# ▪ Local names on a function invocation
# ▪ There is no relation between names in different namespaces

"Namespace order:"

# Built-in Namespace
# Module: Global Namespace
# Function: Local Namespace


"What is a Scope?"

# A region in a program where a namespace is directly accessible

# ▪ In most of the cases, there are at least three nested scopes:

# ▪ The innermost is checked first
# ▪ The scopes of any enclosing functions
# ▪ The next-to-last scope (module's global names)
# ▪ The outermost (built-in names)


# Scopes example:

# Local Scope:
#
# def scopes():
#     def local_scope():
#         text = "local text"
#
# Nonlocal Scope:
#
# def nonlocal_scope():
#     nonlocal text
#     text = "nonlocal text
#
# Global Scope:
#
# def global_scope():
#     global text
#     text = "global text"
