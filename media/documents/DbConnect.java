/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package finalproject;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;

/**
 *
 * @author Paresh shah
 */
public class DbConnect {
   
    public DbConnect()
    {
       
    }
    
    public static Connection getConnection()
    {
        Connection con=null;
        Statement st;
        String url="jdbc:mysql://localhost:3306/new_schema";
         try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            
           con = DriverManager.getConnection("jdbc:mysql://localhost:3306/new_schema","root","root");
           System.out.println("Connection created!!");
           st =  con.createStatement();
           System.out.println("Statement created");
        }catch(Exception ex){
            System.out.println("Erro:"+ex);
        }
        return con;
         
    }
    
    
}
