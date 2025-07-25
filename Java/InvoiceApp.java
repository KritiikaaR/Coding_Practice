import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


class InvoiceFrame extends JFrame{
	public InvoiceFrame() {
		setTitle("Invoice Total Calculator");   //setting the title of the window
		setSize(250,200);   //setting the size 
		setLocationRelativeTo(null);  //to center the window on the screen
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);      //closing the window when user clicks the close button
        setResizable(false);  //prevent from resizing the window
        add(new InvoicePanel());  //add invoice panel to the frame
        setVisible(true);  //make the frame visible
	}
	
}

class InvoicePanel extends JPanel implements ActionListener{
	private JTextField subtotalField;
	private JTextField discountPercentField;
	private JTextField discountAmtField;
	private JTextField invoiceTotalField;
	private JButton calculateButton;
	private JButton exitButton;

	public InvoicePanel() {
		setLayout(new FlowLayout());  //Using FlowLayout
	
		
		//Adding labels and setting the text fields
		add(new JLabel("Subtotal:"));
		subtotalField=new JTextField(10);
		add(subtotalField);
		
		add(new JLabel("Discount Percent"));
		discountPercentField=new JTextField(10);
		discountPercentField.setEditable(false);
		add(discountPercentField);
		
		add(new JLabel("Discount:"));
		discountAmtField=new JTextField(10);
		discountAmtField.setEditable(false);
		add(discountAmtField);
		
		add(new JLabel("Invoice Total:"));
		invoiceTotalField=new JTextField(10);
		invoiceTotalField.setEditable(false);
		add(invoiceTotalField);
		
		//calculate and exit button
		calculateButton=new JButton("Calculate");
		calculateButton.addActionListener(this);
		add(calculateButton);

		exitButton=new JButton("Exit");
		exitButton.addActionListener(this);
		add(exitButton);
		
	}
	
	public void actionPerformed(ActionEvent e) {
		//If Exit button is clicked, close the application
		if (e.getSource() == exitButton) {
            System.exit(0);
        } 
		//If Calculate button is clicked
		else if (e.getSource() == calculateButton) {
        	
			//reading the sub total and converting into number by using parseDouble
			double subtotal = Double.parseDouble(subtotalField.getText());
        	double discountPercent;
        	
        	//Discount percent based on sub total amount
        	if (subtotal >= 200) {
                discountPercent = 0.20;
            } else if (subtotal >= 100) {
                discountPercent = 0.10;
            } else {
                discountPercent = 0.0;
            }
        	
        	//calculating discount amount and final invoice total
        	double discount = subtotal * discountPercent;
        	double total = subtotal - discount;
        	
        	//displaying the results in the text fields and formatting it to 2 decimal places
        	discountPercentField.setText(String.format("%.2f", discountPercent));
        	discountAmtField.setText(String.format("%.2f", discount));
        	invoiceTotalField.setText(String.format("%.2f", total));
        }
	}
}


public class InvoiceApp {
	public static void main(String[] args) {
		
		//displaying the main application window
		new InvoiceFrame();
	}
}
