import torch

lstm_cell = torch.nn.LSTMCell(input_size=3, hidden_size=3)
lstm_cell(torch.randn(3), torch.zeros(2, 3, 3))
