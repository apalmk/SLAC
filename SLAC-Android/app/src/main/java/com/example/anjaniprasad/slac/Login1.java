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

public class Login1 extends AppCompatActivity {
String username,password;
DatabaseReference drr;
List<Teacher> teacherList;
int flag;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login1);
        Intent intent = getIntent();
        teacherList= new ArrayList<>();
        flag =0;
        Bundle extras = intent.getExtras();
        username= extras.getString("username");
        password= extras.getString("password");
        drr = FirebaseDatabase.getInstance().getReference("teacher");
    }

    @Override
    protected void onStart() {
        super.onStart();
        drr.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                teacherList.clear();
                for (DataSnapshot dataSnapshot1:dataSnapshot.getChildren())
                {
                    Teacher t1=dataSnapshot1.getValue(Teacher.class);
                    String usern=t1.getName();
                    String passw=t1.getPass();
//                    Toast.makeText(getApplicationContext(), passw, Toast.LENGTH_LONG).show();
                    if(username.equalsIgnoreCase(usern))
                    {
                        flag=1;
                        if(passw.equals(password))
                        {
                            Intent start = new Intent(Login1.this,PostLogin.class);
                            startActivity(start);
                        }
                        else{
                            flag=2;
                        }
                        break;
                    }
                    teacherList.add(t1);
                }
                if(flag==2)
                {
                    Toast.makeText(getApplicationContext(), "Wrong Password", Toast.LENGTH_LONG).show();
                    Intent start = new Intent(Login1.this,Login.class);
                    startActivity(start);

                }

                if(flag==0)
                {
                    Toast.makeText(getApplicationContext(), "NO such user Present", Toast.LENGTH_LONG).show();
                    Intent start = new Intent(Login1.this,Login.class);
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
