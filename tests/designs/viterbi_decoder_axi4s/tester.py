import cocotb
from cocotb.triggers import Timer

@cocotb.test()
def dut_test(dut):

	yield Timer(100)

	cocotb.result.TestSuccess
