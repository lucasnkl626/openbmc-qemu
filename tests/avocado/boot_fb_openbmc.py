# Test that Facebook machine types boot successfully.
#
# Copyright (c) Meta Platforms, Inc. and affiliates. (http://www.meta.com)
#
# Author:
#   Peter Delevoryas <pdel@fb.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
# This work is licensed under the terms of the GNU GPL, version 2 or
# later.  See the COPYING file in the top-level directory.

from avocado_qemu import QemuSystemTest, wait_for_console_pattern

class BootFbOpenBMC(QemuSystemTest):
    def test_openbic(self):
        """
        :avocado: tags=arch:arm
        :avocado: tags=machine:ast1030-evb
        """
        kernel_url = 'https://github.com/peterdelevoryas/OpenBIC/releases/download/oby35-cl-2022.13.01/Y35BCL.elf'
        kernel_hash = '017edb61244c609de7b5cd8c19258e961aecae902aba8303e6d4351868184ab6'
        kernel_path = self.fetch_asset(kernel_url, asset_hash=kernel_hash, algorithm='sha256')

        self.vm.set_console()
        self.vm.add_args('-kernel', kernel_path)
        self.vm.launch()
        wait_for_console_pattern(self, "uart:~$", failure_message="Failed to find OpenBIC uart prompt.", vm=self.vm)
