class Process_control_block:
    def __init__(self,process):
        self.process_state = process._state
        self.process_program_counter = process._program_counter
        self.cpu_registers
        self.cpu_scheduling_information
        self.memory_management_informtion
        self.accounting_information
        self.io_status_information
