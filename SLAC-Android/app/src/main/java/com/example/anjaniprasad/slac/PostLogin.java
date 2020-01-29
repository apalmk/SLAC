package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

import static android.widget.Toast.LENGTH_LONG;

public class PostLogin extends AppCompatActivity {
DatabaseReference drr1;
String abn,att,lcel,lctt,mood,sa;
List<Classdet> clsdet;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_post_login);
        clsdet= new ArrayList<>();
        drr1 = FirebaseDatabase.getInstance().getReference("Classes");

    }


    @Override
    protected void onStart() {
        super.onStart();
        drr1.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                clsdet.clear();
                for (DataSnapshot dataSnapshot1:dataSnapshot.getChildren())
                {
                    Classdet d1=dataSnapshot1.getValue(Classdet.class);
//                    String usern=t1.getName();
//                    System.out.println("Working");

                    abn=d1.getAbn();
                    att=d1.getAtt();
                    lcel=d1.getLcel();
                    lctt= d1.getLct1();
                    System.out.println("this "+lctt);
                    mood=d1.getMood();
                    sa=d1.getSa();
//                    Toast.makeText(PostLogin.this,lctt,LENGTH_LONG).show();

                    clsdet.add(d1);
                }


            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }



    public void lct(View view)
    {
//        Classdet c1= clsdet.get(0);
//        String lcty=c1.getLct1();
//        Toast.makeText(this,"this"+lctt, LENGTH_LONG).show();
        Intent myIntent = new Intent(PostLogin.this, Lct.class);
        myIntent.putExtra("low",lctt);
        PostLogin.this.startActivity(myIntent);
    }
    public void mood1(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Mood.class);
        myIntent.putExtra("mood",mood);
        //gives the percentages of various moods shown in the class, has yawning and distracted also
        PostLogin.this.startActivity(myIntent);
    }

    public void atten(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Attendanc.class);
        myIntent.putExtra("atten",att);
        //gives the Attendance rooster of the class
        PostLogin.this.startActivity(myIntent);
    }

    public void fin(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Find.class);
        //gives the name of the student from the image sent to the server
//        myIntent.putExtra("",);
        PostLogin.this.startActivity(myIntent);
    }

    public void ear(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Ear.class);
        //gives the names of the students that came late or left early from the class
        myIntent.putExtra("lcel",lcel);
        PostLogin.this.startActivity(myIntent);
    }

    public void ab(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Ab.class);
        myIntent.putExtra("ab",abn);
        //Shows true if any face is new in class or isnot detected
        PostLogin.this.startActivity(myIntent);
    }

    public void sar(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, Sar.class);
        myIntent.putExtra("sa",sa);
        //This shows the ratio of total no of students that slept to that of the students that didn't sleep in the class
        PostLogin.this.startActivity(myIntent);
    }

    public void log(View view)
    {
        Intent myIntent = new Intent(PostLogin.this, MainActivity.class);
        //This shows the ratio of total no of students that slept to that of the students that didn't sleep in the class
        PostLogin.this.startActivity(myIntent);
    }
    @Override
    public void onBackPressed() {

        Toast.makeText(getApplicationContext(),"Click on logout to go back" , Toast.LENGTH_SHORT).show();
    }
}
