Currency Converter with GUI and Graph Visualization
This project is a Currency Converter application built using Python and the Tkinter library for the graphical user interface. It enables users to seamlessly convert currencies and visualize historical exchange rates through an integrated graph feature.

Key Features
User-Friendly GUI:

A clean and interactive Tkinter-based interface.
Dropdown menus for selecting base and target currencies.
Input field for entering the amount to be converted.
Real-time conversion display.
Graph Visualization:

A dynamic graph to display historical exchange rate trends.
Helps users analyze currency performance over time.
Uses libraries like Matplotlib for plotting graphs directly in the application.
Live Exchange Rates:

Fetches real-time exchange rates using an external API (e.g., OpenExchangeRates, CurrencyLayer, or similar).
Ensures up-to-date conversion accuracy.
Error Handling:

Provides feedback for invalid inputs or connectivity issues.
Displays appropriate error messages for unsupported currencies.
Technical Highlights
Tkinter GUI:

Combines labels, buttons, dropdown menus, and input fields for a functional design.
Includes a "Convert" button to trigger the calculation.
Graph Plotting:

Uses Matplotlib to render a line chart showing exchange rate trends.
Embedded directly into the Tkinter GUI using FigureCanvasTkAgg.
Backend Logic:

Leverages Python functions to handle API calls and perform currency conversions.
Implements robust logic for data parsing and formatting.
Potential Use Cases
Currency conversion for travelers.
Quick financial calculations for business professionals.
Visual analysis of currency trends for financial research.
