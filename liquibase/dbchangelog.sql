-- liquibase formatted sql

-- changeset vscode:1663267911509-1
CREATE TABLE "public"."users" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "email" VARCHAR, "hashed_password" VARCHAR, "is_active" BOOLEAN, CONSTRAINT "users_pkey" PRIMARY KEY ("id"));

-- changeset vscode:1663267911509-2
CREATE TABLE "public"."items" ("id" INTEGER GENERATED BY DEFAULT AS IDENTITY NOT NULL, "title" VARCHAR, "description" VARCHAR, "owner_id" INTEGER, CONSTRAINT "items_pkey" PRIMARY KEY ("id"));

-- changeset vscode:1663267911509-3
CREATE UNIQUE INDEX "ix_users_email" ON "public"."users"("email");

-- changeset vscode:1663267911509-4
CREATE INDEX "ix_items_description" ON "public"."items"("description");

-- changeset vscode:1663267911509-5
CREATE INDEX "ix_items_title" ON "public"."items"("title");

-- changeset vscode:1663267911509-6
ALTER TABLE "public"."items" ADD CONSTRAINT "items_owner_id_fkey" FOREIGN KEY ("owner_id") REFERENCES "public"."users" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION;
