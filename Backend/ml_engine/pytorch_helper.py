from pathlib import Path
import torch


def save_model(modl: torch.nn.Module,
               target_dir: str,
               model_name: str) -> None:
    
    """ Save a PyTorch model to the specified directory with the given name.    
    Args:
        modl (torch.nn.Module): The PyTorch model to be saved.
        target_dir (str): The directory where the model will be saved.
        model_name (str): The name of the saved model file.
    """


    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)
    model_path = target_dir_path / model_name
    torch.save(modl.state_dict(), model_path)
    print(f"Model saved to {model_path}")