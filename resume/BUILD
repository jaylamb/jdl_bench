load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "generate_resume",
    srcs = ["generate_resume.py"],
    data = [
        "resume.tex",
        "resume_commands.tex",
        "section/education.tex",
        "section/experience.tex",
        "section/defines.tex",
        "section/skills.tex",
    ],
    deps = [
        requirement("rich"),
    ],
)
