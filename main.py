import libcnb
import toml

def detector(context: libcnb.DetectContext) -> libcnb.DetectResult:
    project_descriptor = context.application_dir / "project.toml"
    result = libcnb.DetectResult()
    if project_descriptor.exists():
        project_content = toml.load(project_descriptor)
        try:
            project_content["io"]["buildpacks"]["processes"]
        except (KeyError, TypeError) as e:
            pass
        else:
            result.passed = True
    return result


def builder(context: libcnb.BuildContext) -> libcnb.BuildResult:
    print("Running Proc Descriptor Buildpack")
    project_descriptor = context.application_dir / "project.toml"
    result = libcnb.BuildResult()
    processes = toml.load(project_descriptor)["io"]["buildpacks"]["processes"]
    print(f"Detected {len(processes)} processes")
    result_processes = result.launch_metadata.processes
    for process in processes:
        result_processes.append(libcnb.Process.parse_obj(process))
        print(f"Added process: { result_processes[-1]}")
    return result


if __name__ == "__main__":
    libcnb.run(detector=detector, builder=builder)
