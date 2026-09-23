load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "generate_resume",
    srcs = ["generate_resume.py"],
    deps = [
        requirement("rich"),
    ],
)
