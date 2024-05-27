# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Capio(CMakePackage):
    """
    CAPIO (Cross-Application Programmable I/O), is a middleware 
    aimed at injecting streaming capabilities to workflow steps 
    without changing the application codebase. It has been 
    proven to work with C/C++ binaries, Fortran Binaries, JAVA, 
    python and bash.
    """
    homepage = "https://github.com/High-Performance-IO/capio"
    git = "https://github.com/High-Performance-IO/capio"

    maintainers("marcoSanti", "GlassOfWhiskey")

    license("MIT", checked_by="marcoSanti")

    version("1.0.0", commit="756e70a")


    depends_on("mpi", type=("build", "run", "link"))
    depends_on("capstone", type=("build", "link", "run", "test"))
    depends_on("cmake", type="build")

    #OS compatibility is only with Linux
    conflicts("platform=darwin", msg="CAPIO is not supported on MacOS")
    conflicts("platform=windows", msg="CAPIO is not supported on Windows")

    #Architecture supported is only x86
    conflicts("arch=aarch64", msg="CAPIO is not yet supported on ARM architectures")
    conflicts("arch=riscv", msg="CAPIO is not yet supported on RISC-V architectures")

    #Variants for Release and Debug
    variant("build_type", default="RelWithDebInfo", description="CMake build type", values=("Release", "Debug"))

    def setup_build_environment(self, env):
        env.set("CPATH", self.spec['capstone'].prefix + "/include/capstone")

    def cmake_args(self):
        args = [
                self.define("CAPIO_LOG", "logs")
             ]
        return args


    def install(self, spec, prefix):
        cmake()
        make()
        install()

