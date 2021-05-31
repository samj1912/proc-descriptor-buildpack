# Proc Descriptor Buildpack

![Version](https://img.shields.io/badge/dynamic/json?url=https://cnb-registry-api.herokuapp.com/api/v1/buildpacks/sam/proc-descriptor&label=Version&query=$.latest.version)

This is a [Cloud Native Buildpack](https://buildpacks.io) that configures [processes](https://github.com/buildpacks/spec/blob/main/buildpack.md#launchtoml-toml) using a [project descriptor](https://github.com/buildpacks/spec/blob/main/extensions/project-descriptor.md#project-descriptor) file - `project.toml`

## Usage

The buildpack automatically generates a host key when you run a build:

```bash
pack build --buildpack sam/proc-descriptor myapp
```

You can customize the SSH configuration by creating a `project.toml` file in your application, and a table like:

```toml
[[io.buildpacks.processes]]
type = "<process type>"
command = "<command>"
args = ["<arguments>"]
direct = false
default = false
```

The keys in the `io.buildpacks.processes` table map directly to [the keys described here.](https://github.com/buildpacks/spec/blob/main/buildpack.md#launchtoml-toml)

## Example

For example create a `project.toml` file with the following content - 

```
[[io.buildpacks.processes]]
type = "web"
command = "echo"
args = ["hello"]
direct = true

[[io.buildpacks.processes]]
type = "another-echo"
command = "echo"
args = ["$MYVAR"]
direct = false
default = false
```

Then run - 

```bash
pack build --buildpack sam/proc-descriptor myapp
docker run myapp
docker run --entrypoint another-echo -e MYVAR=hello myapp
```

