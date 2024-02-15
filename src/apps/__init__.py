from os import listdir

__all__ = [file[:-3] for file in listdir('/apps') if file.endswith('.py') and not file.startswith('__')]