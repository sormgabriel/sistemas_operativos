class Process_test(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		pass
	

	def test1_a(self):
		process= Process new(program_counter,registers,variables)
		pc= process._program_counter()
		cpu.load(process)
		assertEqual(process._program_counter(),cpu._program_counter())
		cpu.run_process()
		assertNotEqual(pc, cpu._program_counter())
		assertEqual(process._program_counter(), cpu._program_counter())


    	def test1():
        	pass



if __name__ == '__main__':



