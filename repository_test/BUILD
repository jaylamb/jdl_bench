load("@my_deps//:requirements.bzl", "requirement")

py_binary(
    name = "test_script",
    srcs = ["test_script.py"],
    deps = [
        requirement("requests"),
        requirement("pandas"),
        requirement("numpy"),
        ]
)