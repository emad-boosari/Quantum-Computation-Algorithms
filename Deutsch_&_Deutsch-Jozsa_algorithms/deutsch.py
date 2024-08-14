{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPadvA00NbUgLNXFFD3eRRE"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["!pip install qiskit\n","!pip install pylatexenc"],"metadata":{"id":"vrOoiJJDOLRP"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["from qiskit import QuantumCircuit\n","import numpy as np"],"metadata":{"id":"uqjopD21OEr8","executionInfo":{"status":"ok","timestamp":1723644591158,"user_tz":-120,"elapsed":948,"user":{"displayName":"Emad Rezaei Fard Boosari","userId":"06573859078457009425"}}},"execution_count":3,"outputs":[]},{"cell_type":"code","execution_count":4,"metadata":{"id":"NaWCc8o4kbi7","executionInfo":{"status":"ok","timestamp":1723645416622,"user_tz":-120,"elapsed":291,"user":{"displayName":"Emad Rezaei Fard Boosari","userId":"06573859078457009425"}}},"outputs":[],"source":["class OracleProvider:\n","    \"\"\"Class to provide different types of oracles for the Deutsch and Deutsch-Jozsa algorithms.\"\"\"\n","\n","    def __init__(self, num_qubits: int):\n","        \"\"\"\n","        Initialize the OracleProvider with the number of input qubits.\n","\n","        :param num_qubits: The number of input qubits (not including the output qubit).\n","        \"\"\"\n","        self.num_qubits = num_qubits\n","\n","    def constant_oracle(self, output_value=0) -> QuantumCircuit:\n","        \"\"\"\n","        Create a constant oracle that returns the same output for any input.\n","\n","        :param output_value: 0 or 1, the value the oracle should return for any input.\n","        :return: A Gate representing the constant oracle.\n","        \"\"\"\n","        oracle = QuantumCircuit(self.num_qubits + 1)\n","\n","        if output_value == 1:\n","            oracle.x(self.num_qubits)  # Flip the output qubit to |1> if the constant output is 1.\n","\n","        return oracle.to_gate(label=\"ConstantOracle\")\n","\n","    def balanced_oracle(self) -> QuantumCircuit:\n","        \"\"\"\n","        Create a balanced oracle that returns 0 for half the inputs and 1 for the other half.\n","\n","        :return: A Gate representing the balanced oracle.\n","        \"\"\"\n","        oracle = QuantumCircuit(self.num_qubits + 1)\n","\n","        # Apply CNOT gates to entangle each input qubit with the output qubit.\n","        for qubit in range(self.num_qubits):\n","            oracle.cx(qubit, self.num_qubits)\n","\n","        return oracle.to_gate(label=\"BalancedOracle\")\n","\n","    def random_oracle(self) -> QuantumCircuit:\n","        \"\"\"\n","        Create a random oracle that is either constant or balanced, but the type is not revealed.\n","\n","        :return: A Gate representing the random oracle.\n","        \"\"\"\n","        if np.random.rand() > 0.5:\n","            return self.constant_oracle(output_value=np.random.randint(2))\n","        else:\n","            return self.balanced_oracle()"]},{"cell_type":"code","source":[],"metadata":{"id":"itzy2atWRdH_"},"execution_count":null,"outputs":[]}]}