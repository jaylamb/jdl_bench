load("@my_deps//:requirements.bzl", "requirement")

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
)