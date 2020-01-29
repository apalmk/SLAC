package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class Login2 extends AppCompatActivity {
    String username1,password1;
    DatabaseReference drro;
    List<Student> studentList;
    int flagg;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login2);
        Intent intent = getIntent();
        studentList= new ArrayList<>();
        flagg =0;
        Bundle extras = intent.getExtras();
        username1= extras.getString("username");
        password1= extras.getString("password");
        drro = FirebaseDatabase.getInstance().getReference("student");
    }

    @Override
    protected void onStart() {
        super.onStart();
        drro.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                studentList.clear();
                for (DataSnapshot dataSnapshot1:dataSnapshot.getChildren())
                {
                    Student s1=dataSnapshot1.getValue(Student.class);
                    String usern=s1.getName();
                    String passw=s1.getPass();
//                    Toast.makeText(getApplicationContext(), passw, Toast.LENGTH_LONG).show();
                    if(username1.equalsIgnoreCase(usern))
                    {
                        flagg=1;
                        if(passw.equals(password1))
                        {
                            Intent start = new Intent(Login2.this,PostLogin1.class);
                            start.putExtra("name",username1);
                            startActivity(start);
                        }
                        else{
                            flagg=2;
                        }
                        break;
                    }
                    studentList.add(s1);
                }
                if(flagg==2)
                {
                    Toast.makeText(getApplicationContext(), "Wrong Password", Toast.LENGTH_LONG).show();
                    Intent start = new Intent(Login2.this,Login.class);
                    startActivity(start);

                }

                if(flagg==0)
                {
                    Toast.makeText(getApplicationContext(), "NO such user Present", Toast.LENGTH_LONG).show();
                    Intent start = new Intent(Login2.this,Login.class);
                    startActivity(start);
                }
//                for()
//                {
//
//                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }
}
