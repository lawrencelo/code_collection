package day12inheritance;

import java.util.*;

class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;
	
	// Constructor
	Person(String firstName, String lastName, int identification){
		this.firstName = firstName;
		this.lastName = lastName;
		this.idNumber = identification;
	}
	
	// Print person data
	public void printPerson(){
		 System.out.println(
				"Name: " + lastName + ", " + firstName 
			+ 	"\nID: " + idNumber); 
	}
	 
}

class Student extends Person{
	private int[] testScores;

    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
	Student(String firstName, String lastName, int identification, int[] testScoreInput) {
		super(firstName, lastName, identification);
		this.testScores = testScoreInput;
	}

    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
	String calculate() {
		int Avg;
		int Sum;
		String grade;
		Avg = 0;
		Sum = 0;
		for(int i = 0; i < testScores.length; i++){
			Sum += testScores[i] ;
		}
		Avg = Sum / testScores.length;
		
		if (Avg >= 90) {
            grade = "O";
        } else if (Avg >= 80) {
            grade = "E";
        } else if (Avg >= 70) {
            grade = "A";
        } else if (Avg >= 55) {
            grade = "P";
        } else if (Avg >= 40) {
            grade = "D";
        } else {
            grade = "T";
        }
		return grade;
	}
}

class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String firstName = scan.next();
		String lastName = scan.next();
		int id = scan.nextInt();
		int numScores = scan.nextInt();
		int[] testScores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			testScores[i] = scan.nextInt();
		}
		scan.close();
		
		Student s = new Student(firstName, lastName, id, testScores);
		s.printPerson();
		System.out.println("Grade: " + s.calculate() );
	}
}
