import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, IconButton, Menu, MenuItem, Link, Box } from '@mui/material';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { useThemeContext } from './ThemeContext'; // Import the ThemeContext
import { Link as RouterLink } from 'react-router-dom'; // For navigation

const Navbar: React.FC = () => {
    const { darkMode, toggleDarkMode } = useThemeContext();
    const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

    const handleMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    return (
        <Box
            sx={{
                position: 'sticky',
                top: 0,
                left: 0,
                right: 0,
                zIndex: 10,
                borderRadius: '0px 0px 20px 20px', // Rounded bottom corners
                background: 'linear-gradient(to right, #9c27b0, #ff9800)', // Purple to Orange gradient
                padding: 1,
                boxShadow: '0px 4px 6px rgba(0,0,0,0.1)',
            }}
        >
            <AppBar position="static" sx={{ background: 'transparent', boxShadow: 'none' }}>
                <Toolbar sx={{ justifyContent: 'space-between' }}>
                    {/* Left Side: Logo and Title */}
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <Box
                            component="img"
                            src="/logo512.png" // Replace with the actual logo path
                            alt="logo"
                            sx={{ height: 40 }}
                        />
                        <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                            Decomplexify
                        </Typography>
                    </Box>

                    {/* Right Side: Links and Account Icon */}
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                        <Link
                            component={RouterLink}
                            to="/"
                            color="inherit"
                            underline="none"
                            sx={{
                                fontWeight: 'bold',
                                fontSize: '1rem',
                                '&:hover': {
                                    textDecoration: 'underline',
                                },
                            }}
                        >
                            Home
                        </Link>
                        <Link
                            component={RouterLink}
                            to="/create"
                            color="inherit"
                            underline="none"
                            sx={{
                                fontWeight: 'bold',
                                fontSize: '1rem',
                                '&:hover': {
                                    textDecoration: 'underline',
                                },
                            }}
                        >
                            Create
                        </Link>
                        <Link
                            component={RouterLink}
                            to="/data"
                            color="inherit"
                            underline="none"
                            sx={{
                                fontWeight: 'bold',
                                fontSize: '1rem',
                                '&:hover': {
                                    textDecoration: 'underline',
                                },
                            }}
                        >
                            Data
                        </Link>
                        <Link
                            component={RouterLink}
                            to="/help"
                            color="inherit"
                            underline="none"
                            sx={{
                                fontWeight: 'bold',
                                fontSize: '1rem',
                                '&:hover': {
                                    textDecoration: 'underline',
                                },
                            }}
                        >
                            Help
                        </Link>
                        <IconButton color="inherit" onClick={handleMenuOpen}>
                            <AccountCircleIcon />
                        </IconButton>
                        <Menu
                            anchorEl={anchorEl}
                            open={Boolean(anchorEl)}
                            onClose={handleMenuClose}
                        >
                            <MenuItem onClick={toggleDarkMode}>
                                {darkMode ? 'Light Mode' : 'Dark Mode'}
                            </MenuItem>
                        </Menu>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    );
};

export default Navbar;
