import torch

log_probs = torch.randn(5, 6, requires_grad=True)
targets = torch.tensor([[3, 5, 6, 7]])
input_lengths = torch.tensor([5])
target_lengths = torch.tensor([4])

loss = torch.nn.functional.ctc_loss(
    log_probs,
    targets,
    input_lengths,
    target_lengths=target_lengths,
)
loss.backward()
