package com.example.anjaniprasad.slac;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class Ab extends AppCompatActivity {
TextView tv3;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ab);
        tv3=(TextView)findViewById(R.id.ab_text);
        Intent iin4= getIntent();
        Bundle b = iin4.getExtras();

        if(b!=null)
        {
            String j =(String) b.get("ab");
//            Toast.makeText(this,j,Toast.LENGTH_LONG).show();
            tv3.setText(j);
        }
    }
    @Override
    public void onBackPressed() {
        Intent myIntent = new Intent(Ab.this, PostLogin.class);
        Ab.this.startActivity(myIntent);
    }
}
