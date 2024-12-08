import React from "react";
import { Box, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography, Paper } from "@mui/material";
import { useTheme } from '@mui/material/styles';

// Define types for the props that this component will receive
interface DynamicTableProps {
  columns: string[];
  data: (string | number | null)[][];
}

const DynamicTable: React.FC<DynamicTableProps> = ({ columns, data }) => {
  const theme = useTheme();
  return (
      <Box sx={{ width: '100%', overflow: 'auto', backgroundColor: 'background.default', padding: 2 }}>
        {data.length > 0 ? (
          <TableContainer component={Paper} sx={{ boxShadow: 3 }}>
            <Table sx={{ minWidth: 650 }} aria-label="dynamic table">
              <TableHead>
                <TableRow>
                  {columns.map((col, index) => (
                    <TableCell key={index} sx={{
                      fontWeight: 'bold', 
                      color: theme.palette.mode === 'dark' ? 'white' : 'black', // Dynamic text color based on theme mode
                      }}>
                      {col}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {data.map((row, rowIndex) => (
                  <TableRow key={rowIndex}>
                    {row.map((cell, cellIndex) => (
                      <TableCell key={cellIndex} sx={{
                        color: theme.palette.mode === 'dark' ? 'white' : 'black', // Dynamic text color based on theme mode
                        }}>
                        {cell}
                      </TableCell>
                    ))}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        ) : (
          <Typography variant="h6" color="text.secondary">
            No data fetched yet.
          </Typography>
        )}
      </Box>
  );
};

export default DynamicTable;