from typing import List, Optional

# Bot token from Bot Father
TOKEN: str = "1690629204:AAG64uwXAVy6OcpC8JAVgM2flrXf8Pjl2jg"

# Your API ID and API HASH
# Get it from https://my.telegram.org/apps
API_ID: int = 1711524
API_HASH: str = "c93b573669b12ffd1c099f62690a2ef6"


# Chat used for logs
log_chat: int = 1342146028

# Sudoers and super sudoers
super_sudoers: List[int] = [957539786]
sudoers: List[int] = [957539786]

# Prefixes for commands
# e.g: /command and !command
prefix: List[str] = ["/", "!"]

# List of disabled plugins
disabled_plugins: List[str] = []

# API Keys (Optional)
TENOR_API_KEY: Optional[str] = ""

# All super sudoers should be sudoers as well
sudoers.extend(super_sudoers)
