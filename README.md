# World Rally Cross Championship Management

This is a command-line application developed for managing a World Rally Cross Championship, allowing users to add, delete, update, and view driver details, simulate races, and save/load data to/from text files.

## Features
- **ADD**: Add a new driver with details (name, age, team, car, points).
- **DDD**: Delete a driver by name.
- **UDD**: Update driver details by name.
- **VCT**: View championship standings sorted by points.
- **SRR**: Simulate a random race and assign points (10 for 1st, 7 for 2nd, 5 for 3rd).
- **VRL**: View race details sorted by date using a custom sorting algorithm.
- **STF**: Save driver data to a text file.
- **RFF**: Load driver data from a text file.
- **ESC**: Exit the program.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rushdi-rzx/F1-World-Rally.git
   cd rally-cross-management
   ```
2. Ensure Python 3 is installed.
3. Install the required package:
   ```bash
   pip install tabulate
   ```
4. Run the program:
   ```bash
   python rally_cross.py
   ```

## Usage
- Launch the program to see the console menu.
- Enter the corresponding command (e.g., `ADD`, `VCT`) to perform actions.
- Follow prompts to input data or view results.
- Data is saved in `stf.txt` (driver details) and `data.txt` (race details).

## File Structure
- `rally_cross.py`: Main Python script with all functionality.
- `stf.txt`: Stores driver details.
- `data.txt`: Stores race details.
- `.gitignore`: Ignores text files and Python cache.
- `README.md`: Project documentation.

## Notes
- The program uses a custom bubble sort for sorting races by date (VRL).
- No databases are used; data is stored in text files.
- The `tabulate` library is used for formatting tables.
- Race simulations are limited to September 2022 (days 1–31).

