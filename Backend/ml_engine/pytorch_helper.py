from pathlib import Path
import torch


def save_model(modl: torch.nn.Module,
               target_dir: str,
               model_name: str,
               input_size: int,
               hidden_size: int,
               output_size: int,
               all_words: list,
               tags: list) -> None:
    
    """ Save a PyTorch model to the specified directory with the given name.    
    Args:
        modl (torch.nn.Module): The PyTorch model to be saved.
        target_dir (str): The directory where the model will be saved.
        model_name (str): The name of the saved model file.
    """


    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)
    model_path = target_dir_path / model_name

    data = {
        "model_state": modl.state_dict(),
        "input_layer": input_size,
        "hidden_layer": hidden_size,
        "output_layer": output_size,
        "all_words": all_words,
        "tags": tags
    }
    torch.save(data, model_path)
    print(f"Model saved to {model_path}")