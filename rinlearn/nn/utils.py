import torch
import torch.nn as nn
def spatial_broadcast(x: torch.Tensor, resolution):
    """Broadcast flat inputs to a 2D grid of a given resolution."""
    x = x[:, None, None, :]
    # return np.tile(x, [1, resolution[0], resolution[1], 1])
    return torch.tile(x, [1, resolution[0], resolution[1], 1])

def broadcast_across_batch(inputs, batch_size):
  """Broadcasts inputs across a batch of examples (creates new axis)."""
  return torch.broadcast_to(
      torch.unsqueeze(0),
      size=(batch_size,) + inputs.shape)