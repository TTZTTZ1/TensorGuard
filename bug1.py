import torch
results = dict()
_input_tensor_tensor = torch.rand([5, 5, 5], dtype=torch.complex32)
_input_tensor = _input_tensor_tensor.clone()
p = 1
dim = 2
maxnorm = 1
try:
  results["res_1"] = _input_tensor.renorm(p, dim, maxnorm, )
except Exception as e:
  results["err_1"] = "ERROR:"+str(e)
try:
  results["res_2"] = _input_tensor_tensor.clone().renorm_(p,dim,maxnorm,)
except Exception as e:
  results["err_2"] = "ERROR:"+str(e)

print(results)
